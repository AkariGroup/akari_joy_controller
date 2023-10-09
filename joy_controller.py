import pygame
from akari_client import AkariClient

JOY_RATE = 0.2


def main() -> None:
    pygame.init()
    joystick_count = pygame.joystick.get_count()

    akari = AkariClient()
    joints = akari.joints
    joints.enable_all_servo()
    limit = joints.get_joint_limits()
    joints.set_joint_accelerations(pan=10, tilt=10)
    joints.set_joint_velocities(pan=3, tilt=3)
    joints.move_joint_positions(pan=0, tilt=0, sync=False)
    if joystick_count == 0:
        print("接続されたジョイスティックがありません。")
        print("ジョイスティックをAKARIに接続してください。")
    else:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        # ジョイスティックの名前を表示
        print("ジョイスティック名:", joystick.get_name())

        # イベントループ
        running = True
        while running:
            pos = joints.get_joint_positions()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.JOYAXISMOTION:
                    axis_x = joystick.get_axis(0)  # X軸の値 (-1.0 から 1.0 の範囲)
                    axis_y = joystick.get_axis(1)  # Y軸の値 (-1.0 から 1.0 の範囲)
                    pos["pan"] = pos["pan"] - axis_x * JOY_RATE
                    pos["tilt"] = pos["tilt"] - axis_y * JOY_RATE
                    # リミット範囲内に収める
                    if pos["pan"] < limit["pan"][0]:
                        pos["pan"] = limit["pan"][0]
                    elif pos["pan"] > limit["pan"][1]:
                        pos["pan"] = limit["pan"][1]
                    if pos["tilt"] < limit["tilt"][0]:
                        pos["tilt"] = limit["tilt"][0]
                    elif pos["tilt"] > limit["tilt"][1]:
                        pos["tilt"] = limit["tilt"][1]
                    joints.move_joint_positions(
                        pan=pos["pan"], tilt=pos["tilt"], sync=False
                    )
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        joints.move_joint_positions(pan=0, tilt=0, sync=False)
    pygame.quit()


if __name__ == "__main__":
    main()
