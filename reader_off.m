function return_dat = reader_off(obj)
	[Status, ResultFlag] = invoke(obj, 'CarrierOnOff', 0);                 % CarrierFlag Off
    return_dat = ResultFlag;