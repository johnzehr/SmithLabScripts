import pyvisa
rm = pyvisa.ResourceManager()
inst = rm.open_resource('TCPIP::169.254.255.125::inst0::INSTR')
def specswitch():
    inst.write(':INST:SEL Spectrum')
def iqswitch():
    inst.write(':INST:SEL IQ')
def startstop(start, stop):
    inst.write("SENS:FREQ:STAR " + start + 'ghz')
    inst.write("SENS:FREQ:STOP " + stop + 'ghz')
def start(start):
    inst.write("SENS:FREQ:STAR " + start + 'ghz')
def stop(stop):
    inst.write("SENS:FREQ:STOP " + stop + 'ghz')
def sweep(time):
    inst.write("SENS:SWE:TIME " + time)
def res(res):
    inst.write("SENS:BAND:RES " + res + 'mhz')
def traceMax():
    inst.write("CALC:HOLD:TYPE MAX")
def traceMin():
    inst.write("CALC:HOLD:TYPE MIN")
def traceClear():
    inst.write("CALC:HOLD:CLE")
def abort():
    inst.write("ABOR")
def avg(avg_num):
    inst.write("SENSE:AVER:TRAC:COUN " + avg_num)
def sweepDelay(num):
    inst.write("SENS:SWE:TRIG:DELay " + num)