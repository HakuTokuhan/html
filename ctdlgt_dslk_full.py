'''
Xây dựng cấu trúc dữ liệu Danh sách Liên kết (DSLK)
'''
from itertools import count
from operator import concat
from unittest import result

from requests import head
from sqlalchemy import null


class PhanTuDSLK:
  def __init__(self, data) -> None:
    self.val = data
    self.ctr = None



class Dslk:
  def __init__(self) -> None:
    self.head = None

  #-- Đếm số phần tử của dslk --
  def do_dai(self):
    cnt = 0
    if (not self.head):
      return 0
    else:
      iter = self.head
      while(iter):
        iter = iter.ctr
        cnt += 1

    return cnt

  ##-- các thao tác trên DSLK --
  def them_cuoi(self, val):
    if (self.head):
      ##- nếu DSLK không rỗng --
      pt = PhanTuDSLK(val)

      iter = self.head
      while (iter.ctr):
        iter = iter.ctr

      iter.ctr = pt
    else:
      ##- nếu DSLK là rỗng --
      pt = PhanTuDSLK(val)
      self.head = pt

  def them_dau(self, val):
    if (self.head):
      ##- nếu DSLK không rỗng --
      pt = PhanTuDSLK(val)

      pt.ctr = self.head
      self.head = pt
    else:
      ##- nếu DSLK là rỗng --
      pt = PhanTuDSLK(val)
      self.head = pt

  def chen_phantu(self, val, i, mode):
    if (self.head):
      ##- nếu DSLK không rỗng --
      pt = PhanTuDSLK(val)

      ##-- kiểm tra chế độ chèn
      ##-- chèn vào trước mode = 't'
      ##-- chèn vào sau mode = 's'
      if (mode == 't'):
        cnt = 1
        iter = self.head
        while(cnt != (i-1)):
          iter = iter.ctr
          cnt += 1        

        pt.ctr = iter.ctr
        iter.ctr = pt
        
      elif (mode == 's'):
        cnt = 0
        iter = self.head
        while(cnt != i):
          iter = iter.ctr
          cnt += 1

        pt.ctr = iter.ctr
        iter.ctr = pt
    
    else:
      ##- nếu DSLK là rỗng --
      pt = PhanTuDSLK(val)
      self.head = pt

  #-- Xóa phần tử đầu DSLK --
  def xoa_dau(self):
    self.head = self.head.ctr

  #-- Xóa phần tử tại vị trí chỉ định trong DSLK --
  def xoa_phantu(self, pos):
    if(pos > self.do_dai()):
      print('vuot qua do dai dslk')
    elif(pos == self.do_dai()):
      self.xoa_cuoi()
    else:
      cnt = 1
      iter = self.head
      while(cnt != (pos-1)):
        iter = iter.ctr
        cnt += 1      
      iter.ctr = iter.ctr.ctr

  #--xóa phần tử cuối DSLK --
  def xoa_cuoi(self):
    iter = self.head
    while (iter.ctr.ctr):
      iter = iter.ctr
    iter.ctr = None

  #-- tìm kiếm theo giá trị --
  def tim_kiem(self, val):
    result = []

    cnt = 0
    iter = self.head
    while(iter):
      cnt += 1
      if(iter.val == val):
        result.append(cnt)
      iter = iter.ctr

    return result


     




##-- hàm main() ---------------------------------------
def main():
  arr = [3, 5, 7 ,8, 10, 100, 2000, 250]
  arr_1 = [2,4,3,9,9,6,1,3,1,1]

  #--  sắp xếp mảng từ nhỏ đến lớn --
  max = 0
  for i in range(len(arr)):
    max = arr[i]
    for j in range(i+1, len(arr)):
      if(max > arr[j]):
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp

  #-- tạo danh sách liên kết với
  #-- các phần tử lấy từ mảng đã sắp xếp
  dslk = Dslk()
  iter = None
  for i in range(len(arr)):
    pt = PhanTuDSLK(arr[i])
    if(dslk.head):
      iter.ctr = pt
      iter = pt
    else:
      dslk.head = pt
      iter = dslk.head

  #-- thêm phần tử vào trước vị trí số 3
  #dslk.chen_phantu(700, 3, 't')

  #-- thêm phần tử vào cuối danh sách --
  #dslk.them_cuoi(1000)

  #-- thêm phần tử vào đầu danh sách --
  #dslk.them_dau(1500)

  #-- xóa phần tử đầu dslk --
  #dslk.xoa_dau()
  #-- xóa phần tử cuối dslk --
  #dslk.xoa_cuoi()
  #-- xóa phần tử tại vị trí 4 trong dslk --
  #dslk.xoa_phantu(4)
  #dslk.xoa_phantu(10)
  #dslk.xoa_phantu(3)
  #-- tìm kiếm các phần tử có giá trị bằng 250 --
  dslk_1 = Dslk()
  iter = None
  for i in range(len(arr_1)):
    pt = PhanTuDSLK(arr_1[i])
    if(dslk_1.head):
      iter.ctr = pt
      iter = pt
    else:
      dslk_1.head = pt
      iter = dslk_1.head

  print(dslk_1.tim_kiem(250))
  print(dslk_1.tim_kiem(1))
  print(dslk_1.tim_kiem(3))

  #-- in danh sách liên kết --
  iter = dslk_1.head
  strDis = ''
  while(iter):
    strDis += '[' + str(iter.val) + '] '
    iter = iter.ctr

  print(strDis)


if __name__ == '__main__':
  main()