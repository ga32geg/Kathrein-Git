function return_dat = reader_on(obj)
	[Status, ResultFlag] = invoke(obj, 'CarrierOnOff', 255);               % CarrierFlag On
    return_dat = ResultFlag;
