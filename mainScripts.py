import pyvisa
def __init__():
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('TCPIP::169.254.255.125::inst0::INSTR')
def specswitch():
    inst.write(':INST:SEL Spectrum')
def iqswitch():
    inst.write(':INST:SEL IQ')
def startstop(start, stop):
    inst.write("SENS:FREQ:STAR " + str(start) + 'ghz')
    inst.write("SENS:FREQ:STOP " + str(stop) + 'ghz')
def start(start):
    inst.write("SENS:FREQ:STAR " + str(start) + 'ghz')
def stop(stop):
    inst.write("SENS:FREQ:STOP " + str(stop) + 'ghz')
def autoSweep():
    inst.write("SENS:SWE:TIME:AUTO ON")
def autoRes():
    inst.write("SENS:BAND:RES:AUTO ON")   
def sweep(time):
    inst.write("SENS:SWE:TIME " + str(time))
def res(res):
    inst.write("SENS:BAND:RES " + str(res) + 'mhz')
def traceClear():
    inst.write("CALC:HOLD:CLE")
def abort():
    inst.write("ABOR")
def avg(avg_num):
    inst.write("SENSE:AVER:TRAC:COUN " + str(avg_num))
def autoAtt():
    inst.write("INP:ATT:AUTO ON")
def setAtt(att):
    inst.write("INP:ATT " +str(att))
def sweepDelay(num):
    inst.write("SENS:SWE:TRIG:DELay " + str(num))
def singleSweep():
    inst.write("INIT:CONT OFF")
def stopSweep():
    inst.write("INIT:IMM;*WAI")
def aveTrace():
    inst.write('DISP:WIND1:SUBW:TRAC1:MODE AVER')
def traceMax():
    inst.write('DISP:WIND1:SUBW:TRAC1:MODE MAXH')
def traceMin():
    inst.write('DISP:WIND1:SUBW:TRAC1:MODE MINH')
def autoOn():
    inst.write('SENS:WIND1:DET1:FUNC AUTO ON')
def autoOff():
    inst.write('SENS:WIND1:DET1:FUNC AUTO OFF')
def detPositive():
    inst.write('SENS:WIND1:DET1:FUNC POS')
def detNegative():
    inst.write('SENS:WIND1:DET1:FUNC NEG')
def detRms():
    inst.write('SENS:WIND1:DET1:FUNC RMS')
def detAutoPeak():
    inst.write('SENS:WIND1:DET1:FUNC APE')
def detAver():
    inst.write('SENS:WIND1:DET1:FUNC AVER')
def detSamp():
    inst.write('SENS:WIND1:DET1:FUNC SAMP')
