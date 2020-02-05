
def main():

        num1 = input("Enter the first number:")

        if not(num1.isdigit()):
                print("The number is invalid ")
        else:
                num2=input("Enter the second number:")
                if not(num2.isdigit()):
                        print("The number is invalid ")
                else:
                        operation=input("Choose the operation (+, -, /, *):")
                        if ( (operation != "+") and (operation != "-") and (operation != "/") and (operation != "*")):
                                print("Operation not valid")
                        elif operation=="+":
                                print("The answar is "+ str(int(num1)+int(num2)))
                        elif operation=="-":
                                print("The answar is "+ str(int(num1)-int(num2)))
                        elif operation=="/":
                                print("The answar is "+ str(int(num1)/int(num2)))
                        elif operation=="*":
                                print("The answar is "+ str(int(num1)*int(num2)))

        #write your code here
        pass




if __name__ == '__main__':
         main()
