import nidaqmx
import time
import nidaqmx.constants as constants
import nidaqmx.system as system

# Define the task name and channel to read from
task_name = "ReadVoltageTask"
task_name2 = "REadTemperatureTask"
channel = "cDAQ9185-1F56937Mod1/ai0"
channel2 = "cDAQ9185-1F56937Mod1/ai1"
channel3 = "cDAQ9185-1F56937Mod1/ai2"


task = nidaqmx.Task(task_name)
#task2 = nidaqmx.Task(task_name2)


# task.ai_channels.add_ai_voltage_chan(physical_channel=channel,
#                                     name_to_assign_to_channel='VoltageChannel',
#                                     terminal_config=constants.TerminalConfiguration.DIFF,
#                                     min_val=-0.125,
#                                     max_val=0.125,
#                                     units=constants.VoltageUnits.VOLTS)
#
task.ai_channels.add_ai_thrmcpl_chan(physical_channel=channel2,
                                      name_to_assign_to_channel='ThermocoupleChannel',
                                      min_val=0,
                                      max_val=100,
                                      units=constants.TemperatureUnits.DEG_C,
                                      thermocouple_type=constants.ThermocoupleType.K,
                                      cjc_source=constants.CJCSource.CONSTANT_USER_VALUE,
                                      cjc_val=25,
                                      cjc_channel='')

task.ai_channels.add_ai_resistance_chan(
        physical_channel=channel3,
        resistance_config=constants.ResistanceConfiguration.FOUR_WIRE,
        current_excit_source=constants.ExcitationSource.INTERNAL,
        current_excit_val=500.0e-6,
        units=constants.ResistanceUnits.OHMS
    )



# while True:
#     task.start()
#     #task2.start()
#
#     voltage = task.read()
#
#     #print("Voltage value: ", voltage[0], "mV")
#     print("Temp value: ", voltage[0], "C")
#     print("Resistance value: ", voltage[1], "Ohms")
#     print("Temp PT value: ", (voltage[1]-100)/0.33, "C")
#
#     time.sleep(0.5)
#
#     task.stop()
#     #task2.stop()
#
# task.stop()
# #task2.stop()
#
# task.close()
# #task2.close()


#create a function that return temperature for pt100
def pt100_temperature():

    task.start()
    temperature = task.read()

    return (temperature[1]-100)/0.33

#create a function that return temperature for thermocouple
def thermocouple_temperature():

        task.start()
        temperature = task.read()

        return temperature[0]


