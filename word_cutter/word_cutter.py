#coding:utf-8
import thulac

if __name__ == '__main__':
    thu1 = thulac.thulac(user_dict=None, model_path=None, T2S=False, seg_only=False, filt=False)  #默认模式
    print(thu1.cut('input.txt'))
