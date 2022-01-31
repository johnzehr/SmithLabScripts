import pyvisa
rm = pyvisa.ResourceManager()
inst=rm.open_resource('TCPIP::169.254.255.125::inst0::INSTR')

def specswitch():
    inst.write(':INST:SEL Spectrum')

def iqswitch():
    inst.write(':INST:SEL IQ')



