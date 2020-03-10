import time,threading,os,requests,multiprocessing
from multiprocessing import Process
from multiprocessing import Pool

url='http://www.yulunan.top'
data={
    'name':'gerh',
    'age':18
}
headerspider = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                # 'Cookie':
                #'Host':
}

def run_proc(name,sleep_time):
    print('Run child process {} {}' .format(name, os.getpid()))
    r = requests.get(url)
    print(r.status_code)
    time.sleep(sleep_time)

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    count_CPU = multiprocessing.cpu_count() //2    #根据CPU数目选择进程数量,6核心12线程会得到CPU数量为12
    p = Pool(count_CPU)
    print('进程数为{}'.format(count_CPU))
    mn = input("输入需要循环的次数")
    m = int(mn)
    sleep_of_time = float(input("输入线程间隔时间"))
    for i in range(m):
        p.apply_async(run_proc, args=(i,sleep_of_time))
    print('Child process will start.')
    p.close()
    p.join()
    print('Child process end.')

    while True:
        contents=input("等待结束指令")
        if contents == 'q':
           break
        else:
            print("无效输入")
    print("循环结束")