import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy 

local= r"C:\Users\omoye\Downloads\locust_output\N1\graphoutput_stats_history.csv"
vmscaleset= r"C:\Users\omoye\Downloads\locust_output\N2\ex2graphoutput_stats_history.csv"
vmscalesetstop= r"\Users\omoye\Downloads\locust_output\N2\ex2graphoutput2_stats_history.csv"
webapp= r"\Users\omoye\Downloads\locust_output\N3\graphoutput_stats_history.csv"
remote= r"\Users\omoye\Downloads\locust_output\N4\ex4output_stats_history.csv"


# plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

pd_local = pd.read_csv(local)[["Requests/s","Failures/s"]]
pd_VMs = pd.read_csv(vmscaleset)[["Requests/s","Failures/s"]]
pd_webapp = pd.read_csv(webapp)[["Requests/s","Failures/s"]]
pd_remote = pd.read_csv(remote)[["Requests/s","Failures/s"]]


figure, axis = plt.subplots(4,1)
axis[0].plot(pd_local)
axis[0].set_title("Local")

axis[1].plot(pd_VMs)
axis[1].set_title("VMs")

axis[2].plot(pd_webapp)
axis[2].set_title("WebApp")

axis[3].plot(pd_remote)
axis[3].set_title("Function")

plt.show()
