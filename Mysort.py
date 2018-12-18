
class MySort(object):
    '''
    data:传入要排序的数据
    isNew:是否返回新的数据，默认在原数据排序，无返回新数据
    isAsce:默认升序，设置为False为降序排列
    '''
    def __init__(self,data,isNew=True,isAsce=True):
        self.data = data
        self.isNew=isNew
        self.isAsce=isAsce
        self.len = len(data)

    def __repr__(self):
        return '<Class Mysort>'

    #冒泡排序
    def bubbleSort(self):
        # 冒泡排序要排序n个数，由于每遍历一趟只排好一个数字，
        # 则需要遍历n-1趟，所以最外层循环是要循环n-1次，而
        # 每次趟遍历中需要比较每归位的数字，则要在n-1次比较
        # 中减去已排好的i位数字，则第二层循环要遍历是n-1-i次
        for i in range(self.len-1):
            for j in range(self.len-1-i):
                if self.data[j] > self.data[j+1]:
                    if self.isAsce:
                        self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
                else:
                    if not self.isAsce:
                        self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        if self.isNew:
            return self.data
        return self

    #选择排序
    def selectSort(self):
        #首先在数据中找到最大的或最小的放在首位置
        #依次对后续为排序的数据找到最大或最小依次放在上述步骤之后

        for i in range(self.len-1):
            index = i
            for j in range(i+1,self.len):
                if not self.isAsce:
                    if self.data[index] < self.data[j]:
                        index = j
                elif self.data[index] > self.data[j]:
                    index = j
            self.data[i],self.data[index] = self.data[index],self.data[i]
        if self.isNew:
            return self.data
        return self

    #插入排序
    def insertSort(self):
        # 首先确定第一个数，后续依次与之前有序序列比较，出入到合适位置
        for j in range(1,self.len):
            i = j
            # i 作为内层循环初始值
            while i > 0:
                # 判断升序（降序）条件
                if self.data[i] < self.data[i-1] and self.isAsce or \
                        (self.data[i] > self.data[i-1] and not self.isAsce):
                    self.data[i],self.data[i-1] = self.data[i-1],self.data[i]
                    i -= 1
                else:
                    break
        if self.isNew:
            return self.data
        return self

    #希尔排序（利用插入排序）
    def sellSort(self):
        #先分布分组，后插入排序
        #减小分步间距，在插入排序
        #只要gap选择合适，效率较插入排序高很多
        gap = self.len // 2
        while gap>0:
            for j in range(gap,self.len):
                i=j
                while i > 0:
                    if self.data[i] < self.data[i-gap] and self.isAsce \
                            or (self.data[i] > self.data[i-gap] and not self.isAsce):
                        self.data[i],self.data[i-gap] = self.data[i-gap],self.data[i]
                        i -= gap
                    else:
                        break
            gap //= 2
        if self.isNew:
            return self.data
        return self

    #快速排序
    def quickSort(self,first,last):
        # 两个下标，直接确定一个数的位置
        # 对于某个数m，定义两个游标，low，high
        # low指定m所在位置，此时为空，暂时不动，让high从右往左，遇到小于m数，移到low位置，此时high为空
        # 移动low，low > m ,将该数放到high位置，此时low为空，移动high
        # ... ...
        # 直到 low 与 high 交会
        # 交会位置即为m排序后应该所在的位置，然后对剩余序列分别做上述工作
        if first >= last:
            return
        mid_value = self.data[first]
        low = first
        high= last
        while low < high:
            # 判断是升序还是降序排序
            if self.isAsce:
                # high左移条件
                while low < high and self.data[high] >= mid_value:
                    high -= 1
                # 移动退出说明high此时的值比min_value 小
                self.data[low] = self.data[high]
                while low < high and self.data[low] < mid_value:
                    low += 1
                self.data[high] = self.data[low]
            else:
                while low < high and self.data[high] <= mid_value:
                    high -= 1
                # 移动退出说明high此时的值比min_value 小
                self.data[low] = self.data[high]
                while low < high and self.data[low] > mid_value:
                    low += 1
                self.data[high] = self.data[low]

        self.data[low] = mid_value
        # 对low左边的进行快排
        self.quickSort(first,low-1)
        # 对low右边的进行快排
        self.quickSort(low+1,last)
        if self.isNew:
            return self.data

    #归并排序
    def mergeSort(self,datalst=False):
        # 对半拆分，然后对应有序合并
        if not datalst:
            datalst = self.data
        mid = len(datalst)//2
        if len(datalst) <= 1:
            return datalst
        #left_list,right_list 采用归并排序后形成的有序新的列表
        left_list = self.mergeSort(datalst[:mid])
        right_list = self.mergeSort(datalst[mid:])

        #将两个有序的子序列合并成一个新的整体
        left_pointer,right_pointer = 0,0
        result = []
        # 循环合并，退出条件是left,right一个为空
        while left_pointer < len(left_list) and right_pointer < len(right_list):
            # 判断升序还是降序排列
            if self.isAsce:
                if left_list[left_pointer] > right_list[right_pointer]:
                    result.append(left_list[left_pointer])
                    left_pointer += 1
                else:
                    result.append(right_list[right_pointer])
                    right_pointer += 1
            else:
                if left_list[left_pointer] < right_list[right_pointer]:
                    result.append(left_list[left_pointer])
                    left_pointer += 1
                else:
                    result.append(right_list[right_pointer])
                    right_pointer += 1
        # 一个为空，将另一个追加到结果中
        result += left_list[left_pointer:]
        result += right_list[right_pointer:]
        return result


if __name__ == '__main__':
    l = [1,10,8,3,5]
    mysort = MySort(l,isAsce=False,isNew=True)
    l1 = mysort.mergeSort()
    print(l1)