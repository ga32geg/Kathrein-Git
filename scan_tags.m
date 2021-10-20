function return_dat = scan_tags(obj)
	[Status, ResultFlag] = invoke(obj, 'CarrierOnOff', 255);               % CarrierFlag On
    [Status, ResultFlag_EPC, Tags] = invoke(obj, 'SyncGetEPCs');           % Tags lesen; Status = 0->Fehler FlagResolve(ResultFlag); Status = 2 Kein Tag; Status = 1 Tag gefunden
	[Status, ResultFlag] = invoke(obj, 'CarrierOnOff', 0);                 % CarrierFlag Off
    
    try
        data = reshape(Tags,1,[]);
        writetable(struct2table(data), 'tags.txt');
        return_dat = size(data);
    catch
        return_dat = ResultFlag_EPC;
    end
