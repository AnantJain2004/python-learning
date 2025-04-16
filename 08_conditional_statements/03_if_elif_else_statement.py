traffic_signal = input("Enter Traffic Signal: ")

if(traffic_signal == "red"):
    print("STOP")
elif(traffic_signal == "yellow"):
    print("WAIT")
elif(traffic_signal == "green"):
    print("GO")
else:
    print("Enter Valid Signal!")