while True:
    try:
         number=int(input("Give a input in number :"))
         print(18/number)
         break
    except ValueError:
         print("make sure your input and enter a Number.")  
    except ZeroDivisionError:
         print("dont pick zero")
    except:
         break
    finally:
         print("loop complete")