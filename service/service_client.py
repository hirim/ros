import rospy
from ros_add.srv import add, addResponse

def add_client(x,y):
    rospy.init_node(“client_node”)
    rospy.wait_for_service(“addition”)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            add_two_ints = rospy.ServiceProxy(“addition”, add)
            response = add_two_ints(x, y)
            rospy.loginfo(response.result)
            rate.sleep()
        except rospy.ServiceException as e:
            print(“service call failed %d”,e)
if __name__ == “__main__”:
    add_client(7, 3)
