def display(data):
    print(f"The area is{data}")

def get_input():
    recived_length=input("length:")
    recived_width=input("width:")
    return (recived_length,recived_width)

def compute_area(length,width):
    area=int(length)*int(width)
    return area
def main():
    length,width=get_input()
    data=compute_area(length,width)
    display(data)
main()
