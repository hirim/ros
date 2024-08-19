import rospy
from ros_add.srv import add, addResponse

def callback(request):
    return addResponse(request.a + request.b)

def add_numbers():
    rospy.init_node(“addition_service”)
    service = rospy.Service(“addition”, add, callback)
    rospy.spin()
if __name__ == “__main__”:
    add_numbers()
