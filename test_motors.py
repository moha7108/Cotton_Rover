import serial
import time

'''
This is an example code for the pico motor driver for mecanum wheels:
available directions: 'forwared', 'backward', 'right', 'left', 'rotate_right', 'rotate_left', 'stop'
available speeds: 0-100  (note that motor start rotating around 30)


serial communication format  send the following command to /dev/ttyAMC0--> 'direction:{direction};speed:{speed}'

'''



def set_speed(ser, direction='forward', speed=50):
    message = f'direction:{direction};speed:{speed}\n'
    ser.write(message.encode('utf-8'))
    ser.reset_input_buffer()

    return message

if __name__=="__main__":

    # Open the serial port
    ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)

    try:
        ## Set direction forward and increment speed from 30 to 100
        for speed in range(30,101):
            message = set_speed(ser, direction='forward', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')

        time.sleep(10)

        ## Set direction forward and increment speed from 100 to 0
        for speed in range(100,-1,-1):
            message = set_speed(ser, direction='forward', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')

        time.sleep(1)

        ## Set direction backward and increment speed from 30 to 100
        for speed in range(30,101):
            message = set_speed(ser, direction='backward', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')

        time.sleep(10)

        ## Set direction backward and increment speed from 100 to 0
        for speed in range(100,-1,-1):
            message = set_speed(ser, direction='backward', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')

        time.sleep(1)

        ## Set direction right and increment speed from 30 to 100
        for speed in range(30,101):
            message = set_speed(ser, direction='right', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')


        time.sleep(10)

        ## Set direction right and increment speed from 100 to 0
        for speed in range(100,-1,-1):
            message = set_speed(ser, direction='right', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')

        time.sleep(1)

        ## Set direction left and increment speed from 30 to 100
        for speed in range(30,101):
            message = set_speed(ser, direction='left', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')


        time.sleep(10)

        ## Set direction left and increment speed from 100 to 0
        for speed in range(100,-1,-1):
            message = set_speed(ser, direction='left', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')

        time.sleep(1)

        ## Set direction rotate right (clockwise) and increment speed from 30 to 100
        for speed in range(30,101):
            message = set_speed(ser, direction='rotate_right', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')


        time.sleep(10)

        ## Set direction rotate right (clockwise) and increment speed from 100 to 0
        for speed in range(100,-1,-1):
            message = set_speed(ser, direction='rotate_right', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')

        time.sleep(1)

        ## Set direction rotate left (counter clockwise) and increment speed from 30 to 100
        for speed in range(30,101):
            message = set_speed(ser, direction='rotate_left', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')


        time.sleep(10)

        ## Set direction rotate right (counter clockwise) and increment speed from 100 to 0
        for speed in range(100,-1,-1):
            message = set_speed(ser, direction='rotate_left', speed=speed)
            time.sleep(.05)
        print(f'set to: {message}')

        time.sleep(1)


    except KeyboardInterrupt:
        # Catch Ctrl+C and send stop command
        try:
            message = set_speed(ser, direction='stop')
            print("\nCtrl+C pressed. Sent stop command.")
        except:
            pass  # In case the serial port was not opened or already closed
        finally:
            print("Stopped by user.")

    except serial.SerialException as e:
        print(f"Serial error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
        print("Serial connection closed.")
