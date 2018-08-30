#!/usr/bin/env python
# -*- coding:utf-8 
# script_name: nginx_log_analysis.py
# function: nginx访问日志分析脚本

import sys, requests, random, json
from time import clock
from datetime import datetime
from collections import Counter


# 该类是用来生成主机信息的字典


class hostInfo(object):
    # 每个主机信息,如某个主机200出现的次数 请求的次数 该主机请求的流量之和
    host_info = ['200', '404', '500', '302', '304', '503', '403', 'times', 'size', 'max_response_time', 'max_call',
                 'response_time', 'api_max_response_time', 'api_max_call', 'api_response_time', 'api_times',
                 'api_failure_times']

    def __init__(self):
        self.host = {}.fromkeys(self.host_info, 0)

    def increment(self, flag, value=None):
        """该方法是用来给host_info中的各个值加1"""
        if flag == 'times':
            self.host['times'] += 1
        elif flag == 'api_times':
            self.host['api_times'] += 1
        elif flag == 'size':
            self.host['size'] = self.host['size'] + value
        else:
            self.host[flag] += 1

    def get_value(self, value):
        """该方法是取到各个主机信息中对应的值"""
        return self.host[value]

    def update(self, flag, value=None):
        """如果当前IP的响应时间比之前的大，就更新"""
        if flag == 'response_time':
            try:
                self.host['response_time'] = float(value) if self.host['response_time'] < value else self.host[
                    'response_time']
            except TypeError:
                pass
        elif flag == 'api_response_time':
            try:
                self.host['api_response_time'] = float(value) if self.host['api_response_time'] < value else self.host[
                    'api_response_time']
            except TypeError:
                pass
        else:
            pass


class fileAnalysis(object):
    def __init__(self):
        """初始化一个空字典"""
        self.report_dict = {}
        self.total_call_time = []
        self.api_total_call_time = []
        self.total_request_times, self.total_traffic, self.total_200, self.total_404, self.total_500, self.total_403, \
        self.total_302, self.total_304, self.total_503, self.max_response_time, self.max_call = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.00, 0
        self.api_total_request_times, self.api_total_ok, self.api_total_false, self.api_max_response_time, self.api_max_call = 0, 0, 0, 0, 0

    def split_line(self, line):
        """分割文件中的每一行，并返回一个字典"""
        split_line = line.split()
        split_dict = {'remote_host': split_line[0], 'status': split_line[8], 'bytes_sent': split_line[9],
                      'call_time': split_line[3][1:],
                      # 'response_time': float(split_line[-1]) if '0.' in split_line[-1] else 0,
                      'response_time': float(split_line[-1]),
                      'url': split_line[6]}
        return split_dict

    def generate_log_report(self, logfile, date):
        """读取文件，分析split_eachline_todict方法生成的字典, 如果有time,那么就找time的，否则要今天的"""
        # 遍历这个日志文件，出现错误的行（如:空行或split拆分时出现错误的行），跳过继续
        for line in logfile:
            try:
                line_dict = self.split_line(line)
                host = line_dict['remote_host']
                status = line_dict['status']
                call_time = line_dict['call_time']
                response_time = line_dict['response_time']
                url = line_dict['url']
            except ValueError:
                continue
            except IndexError:
                continue
            # 如果这个主机（键）在report_dict不存在，就初始化一个该主机的对象，然后把该对象赋值给该键（该主机）
            # 如果存在，那么就取出该主机的值（也就是主机对象）
            # 如果当前的日期和传送的日期一致，那么就执行，否则不执行
            day, month, year_time = call_time.split('/')[:4]
            year = year_time.split(':')[0]
            call_date = day + '/' + month + '/' + year
            if call_date == date:
                if host not in self.report_dict:
                    host_info_obj = hostInfo()
                    self.report_dict[host] = host_info_obj
                else:
                    host_info_obj = self.report_dict[host]

                self.total_call_time.append(call_time)  # 每次请求之后这个把这个请求时间加入，方便以后统计最大并发数
                host_info_obj.increment('times')  # 主机的请求次数进行加1
                host_info_obj.update('response_time', response_time)  # 更新最大响应时长
                if status in host_info_obj.host_info:  # 如果得到的状态在事先定义好的列表里面
                    host_info_obj.increment(status)  # 主机的状态数进行加1
                try:
                    bytes_sent = int(line_dict['bytes_sent'])  # 转换字节为int类型
                except ValueError:
                    bytes_sent = 0
                host_info_obj.increment('size', bytes_sent)  # 主机的访问的字节数

                if (url.find('/api/v1') != -1) or (url.find('/api/v2') != -1):  # 这里都是关于api的
                    self.api_total_call_time.append(call_time)
                    print('api call time:', call_time)
                    host_info_obj.increment('api_times')
                    host_info_obj.update('api_response_time', response_time)  # 更新最大响应时长
                    if status in ('400', '401', '402', '403', '404', '405', '500', '501', '502', '503'):
                        host_info_obj.increment('api_failure_times')


            else:
                continue
        return self.report_dict

    def return_sorted_list(self, true_dict):
        """计算各个状态次数、流量总量，请求的总次数，并且计算各个状态的总量 并生成一个正真的字典，方便排序"""
        for host_key in true_dict:
            host_value = true_dict[host_key]
            times = host_value.get_value('times')  # 每个IP地址请求的次数
            self.total_request_times = self.total_request_times + times  # 各个请求次数之和
            api_times = host_value.get_value('api_times')  # 每个api请求的次数
            self.api_total_request_times = self.api_total_request_times + api_times  # 各个api请求次数之和
            api_failure_times = host_value.get_value('api_failure_times')  # 每个api请求的次数
            self.api_total_false = self.api_total_false + api_failure_times  # 各个api请求失败次数之和
            size = host_value.get_value('size')  # 每个IP地址请求的字节数
            self.total_traffic = self.total_traffic + size  # 各个IP请求字节数之和
            ip_max_response_time = host_value.get_value('response_time')  # 每个IP最大的请求时长
            self.max_response_time = ip_max_response_time if self.max_response_time < ip_max_response_time else self.max_response_time
            api_max_response_time = host_value.get_value('api_response_time')  # 每个API最大的请求时长
            print('every api max call time:', ip_max_response_time)
            self.api_max_response_time = api_max_response_time if self.api_max_response_time < api_max_response_time else self.api_max_response_time
            print('max api max response time: ', self.max_response_time)

            o200 = host_value.get_value('200')
            o404 = host_value.get_value('404')
            o500 = host_value.get_value('500')
            o403 = host_value.get_value('403')
            o302 = host_value.get_value('302')
            o304 = host_value.get_value('304')
            o503 = host_value.get_value('503')

            # 生成一个真正的字典方便排序,这之前主机对应的值其实是一个对象
            true_dict[host_key] = {'200': o200, '404': o404, '500': o500,
                                   '403': o403, '302': o302, '304': o304,
                                   '503': o503, 'times': times, 'size': size}

            # 计算各个状态总量
            self.total_200 = self.total_200 + o200
            self.total_404 = self.total_404 + o404
            self.total_500 = self.total_500 + o500
            self.total_302 = self.total_302 + o302
            self.total_304 = self.total_304 + o304
            self.total_503 = self.total_503 + o503

        # 生成的真正的字典按照先请求次数排序，然后再安装请求的字节数进行排序
        call_counts = Counter(self.total_call_time)
        api_call_counts = Counter(self.api_total_call_time)
        self.max_call = call_counts.most_common(1)[0][1] if len(call_counts.most_common(1)) > 0 else 0
        self.api_max_call = api_call_counts.most_common(1)[0][1] if len(api_call_counts.most_common(1)) > 0 else 0
        sorted_list = sorted(true_dict.items(), key=lambda t: (t[1]['times'], t[1]['size']), reverse=True)

        return sorted_list


# 该类是用来打印格式
class displayFormat(object):
    def format_size(self, size):
        """格式化流量单位"""
        KB = 1024  # KB -> B  B是字节
        MB = 1048576  # MB -> B  1024 * 1024
        GB = 1073741824  # GB -> B  1024 * 1024 * 1024
        TB = 1099511627776  # TB -> B  1024 * 1024 * 1024 * 1024
        if size >= TB:
            size = str(size >> 40) + 'T'
        elif size < KB:
            size = str(size) + 'B'
        elif size >= GB and size < TB:
            size = str(size >> 30) + 'G'
        elif size >= MB and size < GB:
            size = str(size >> 20) + 'M'
        else:
            size = str(size >> 10) + 'K'
        return size

    # 定义字符串格式化
    formatstring = '%-15s %-10s %-12s %8s %10s %10s %10s %10s %10s %10s %10s'

    def transverse_line(self):
        """输出横线"""
        print(self.formatstring % (
            '-' * 15, '-' * 10, '-' * 12, '-' * 12, '-' * 10, '-' * 10, '-' * 10, '-' * 10, '-' * 10, '-' * 10,
            '-' * 10))

    def head(self):
        """输出头部信息"""
        print(self.formatstring % ('IP', 'Traffic', 'Times', 'Times%', '200', '404', '500', '403', '302', '304', '503'))

    def error_print(self):
        """输出错误信息"""
        print('Usage : ' + sys.argv[0] + ' NginxLogFilePath [Number]')
        sys.exit(1)

    def execut_time(self):
        """输出脚本执行的时间"""
        print()
        print("Script Execution Time: %.3f second" % clock())
        print()


def execute():
    """主函数"""

    display_format = displayFormat()
    sys.argv = ['report.py', 'cc.access.log', '30/Jul/2018']
    # 判断命令行参数是否为空及判断命令行传进来的文件是否是有效的文件
    arg_length = len(sys.argv)
    if arg_length == 1:
        display_format.error_print()
    elif arg_length == 2 or arg_length == 3:
        infile_name = sys.argv[1]
        try:
            with open(infile_name, 'r') as infile:
                if arg_length == 3:
                    date = sys.argv[2]
                else:
                    date = datetime.now().strftime('%d/%m/%Y')
                    # 实例化一个fileAnalysis类的对象
                fileAnalysis_obj = fileAnalysis()
                # 调用generate_log_report方法生成字典
                not_true_dict = fileAnalysis_obj.generate_log_report(infile, date)
                # 对上面生成的字典进行排序，生成一个有序列表
                log_report = fileAnalysis_obj.return_sorted_list(not_true_dict)

                total_ip = len(log_report)

            # 打印报告头及横线
            total_traffic = display_format.format_size(fileAnalysis_obj.total_traffic)
            total_request_times = fileAnalysis_obj.total_request_times  # 所有ip全部请求次数
            max_response_time = fileAnalysis_obj.max_response_time  # 所有ip最大响应时间
            max_call = fileAnalysis_obj.max_call  # 所有ip最大并发数
            api_total_request_times = fileAnalysis_obj.api_total_request_times  # 所有API全部请求次数
            api_max_response_time = fileAnalysis_obj.api_max_response_time  # 所有ip最大响应时间
            print('api max_respoonse_time', api_max_response_time)
            api_max_call = fileAnalysis_obj.api_max_call  # 所有ip最大并发数
            api_total_false = fileAnalysis_obj.api_total_false
            print()
            print('查询的日期: %s   IP访问数量: %d   流量传入: %s   上游调用次数: %d  上游故障次数: %d  上游最大响应时间(秒): %s   上游最大并发数(秒): %d' % (
                date, total_ip, total_traffic, total_request_times,
                fileAnalysis_obj.total_403 + fileAnalysis_obj.total_404 + fileAnalysis_obj.total_500,
                str(max_response_time), max_call))
            print()
            print('API调用次数: %d     API故障次数: %d     API接口最大并发数(秒): %d    API接口调用最大响应时长(秒): %s' % (
                api_total_request_times, api_total_false, api_max_call, api_max_response_time
            ))
            print()
            display_format.head()
            display_format.transverse_line()

            # 循环这个列表，打印主机的各个值
            for host in log_report:
                times = host[1]['times']
                times_percent = (float(times) / float(fileAnalysis_obj.total_request_times)) * 100
                print(display_format.formatstring % (host[0],
                                                     display_format.format_size(host[1]['size']),
                                                     times, str(times_percent)[0:5],
                                                     host[1]['200'], host[1]['404'],
                                                     host[1]['500'], host[1]['403'],
                                                     host[1]['302'], host[1]['304'], host[1]['503']))

            display_format.transverse_line()
            print(display_format.formatstring % (total_ip, total_traffic,
                                                 total_request_times, '100%',
                                                 fileAnalysis_obj.total_200,
                                                 fileAnalysis_obj.total_404,
                                                 fileAnalysis_obj.total_500,
                                                 fileAnalysis_obj.total_403,
                                                 fileAnalysis_obj.total_302,
                                                 fileAnalysis_obj.total_304,
                                                 fileAnalysis_obj.total_503))
            # 输出脚本执行的时间
            display_format.execut_time()
        except IOError as e:
            print()
            print(e)
            display_format.error_print()
            raise IOError
        except ValueError:
            print()
            print("Please Enter A Valid Number !!")
            display_format.error_print()
            raise ValueError
    else:
        display_format.error_print()
        raise ValueError


def test_post():
    # 模拟post请求
    # 忽略requests发起post请求时的部分警告
    requests.packages.urllib3.disable_warnings()
    # 登陆URL地址
    login_url = 'https://data.taijihuabao.com/api-auth/'
    # 登陆请求头header
    login_header = {"Content-Type": "application/json"}
    # 登陆请求内容
    login_data = {"username": "tjhb", "password": "daochi12e"}
    try:
        # 获取登陆请求返回的信息
        login_response = requests.post(url=login_url, json=login_data, headers=login_header, verify=False)
        login_response_code = login_response.status_code  # 返回响应码
        login_response_body = login_response.json()  # 返回响应内容
        print('登陆返回响应结果:\n', login_response_code, login_response.ok)
        # 根据返回的结果码判断登陆是否成功：成功---200 ；其他----失败
        if login_response_code.__eq__('200'):
            # 登陆成功，获取返回结果并将返回的token信息放入下次请求的请求头中
            post_header_token = 'JWT ' + login_response_body.get('token')
            # 将token信息放入请求头中
            login_header.setdefault('Authorization', post_header_token)
            # post请求URL地址
            post_url = 'https://data.taijihuabao.com/api/v2/customerauth/verify_nmi/'
            # 请求数据要求，每次请求的手机号后四位随机生成，避免每次查询相同的数据
            mobile = '1823106' + str(random.randint(1000, 9999))
            post_data = {'name': '杜红强', 'id_card': '130434199608187535', 'mobile': mobile}
            try:
                # 发起post请求并获取post请求后的返回信息
                post_response = requests.post(url=post_url, json=post_data, headers=login_header, verify=False)
                # 打印输出post请求的返回结果码
                print('Response code:\n', post_response.status_code, post_response.ok)
                print('Response body:\n', post_response.json())
                nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取现在的时间
                if post_response.status_code.__eq__('200'):
                    print('系统测试成功，当前时间为：', nowTime)
                else:
                    print('Response Code: ', post_response.status_code)
                    print('系统返回错误，请检查。当前时间为： ', nowTime)
                # break
            except requests.RequestException as e:
                print(e)
                return 'ok'
        # else:
        #     continue

        else:
            print('登陆失败')
        return 'ok'

    except requests.RequestException as e:
        print(e)
        return 'ok'
    except ConnectionError as e:
        print(e)
        return 'ok'


if __name__ == '__main__':
    test_post()
    execute()
