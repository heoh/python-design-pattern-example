from car import Car

def main():
    print("차를 제어합니다.")
    
    print("차의 부속품들을 어떻게 제어할지는 신경쓰지 않습니다.")
    car = Car()
    
    car.go_straight()
    car.turn_left()
    car.turn_right()
    car.go_backward()
    car.stop()


if __name__ == '__main__':
    main()
