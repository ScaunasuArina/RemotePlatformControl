import motors
import distance_sensor
 
def auto_drive():
    delay = 0.6
    # read the distance to see if we have obstacles in front of the platform
    distanceF = distance_sensor.read_distance()
    
    # if it is an object detected in front of the platform, we will measure the distances
    # on the right (distanceR) and  left (distanceL)
    if distanceF < 30:
        print('Object detected in front of the car at %.2f cm!' % distanceF)
        motors.turn_right(delay)
        
        distanceR = distance_sensor.read_distance()
        print('On the right side, object detected at %.2f cm'% distanceR)
        
        #  if we have another obstacle on the right side, we turn to left and see if there
        # is another obstacle
        if distanceR < 30:
            motors.turn_left(delay)
            motors.turn_left(delay)
            distanceL = distance_sensor.read_distance()
            print('On the left side, object detected at %.2f cm' % distanceL)
            
            # if we have an obstacle closer on the left side, we will drive through the right side
            if distanceL < distanceR:
                print('Avoiding through the right side')
                motors.turn_right(delay)
                motors.turn_right(delay)
                motors.move_forward(1)
                motors.turn_left(delay)
                # check again if we have avoided the obstacle
                auto_drive()
                
            else:
                print('Avoiding through the left side')
                motors.move_forward(1)
                motors.turn_right(delay)
                # check again if we have avoided the obstacle
                auto_drive()
                
        else:
            print('Avoiding through the right side')
            motors.move_forward(1)
            motors.turn_left(delay)
            auto_drive()
                
    else:
        print('No object in front of the car. Moving forward.')
        motors.move_forward(delay)
        auto_drive()
