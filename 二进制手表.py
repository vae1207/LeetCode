class Solution(object):
    def readBinaryWatch(self, num):
      
        ret = []
        for hour in range(12):
            
            for minute in range(60):
                if(bin(hour) + bin(minute)).count('1') == num:
                    ret.append('%d:%02d' % (hour,minute))
                    
        return ret
    
