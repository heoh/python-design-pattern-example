from motor import Motor

def main():
    print("차를 제어합니다.")

    print("차를 움직이려면 모터를 제어해야 합니다.")
    left_motor = Motor("L Motor")
    right_motor = Motor("R Motor")

    # 전진
    left_motor.set_speed(100)
    right_motor.set_speed(100)

    # 좌회전
    left_motor.set_speed(-50)
    right_motor.set_speed(50)

    # 우회전
    left_motor.set_speed(50)
    right_motor.set_speed(-50)

    # 후진
    left_motor.set_speed(-100)
    right_motor.set_speed(-100)

    # 정지
    left_motor.set_speed(0)
    right_motor.set_speed(0)

if __name__ == '__main__':
    main()
