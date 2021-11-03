function return_dat = reader_init(cw_mode, power_dbm)
    % Initialize Reader
    if exist ('kathreinReader') ~= 0
        delete(kathreinReader);
    end
    kathreinReader = icdevice('kathrein_driver.mdd');
    connect(kathreinReader);

    [Status, ResultFlag] = invoke(kathreinReader, 'SetExtResultFlag', 3);  % RSSI 
    [Status, ResultFlag] = invoke(kathreinReader, 'SetMode', cw_mode);     % NormalMode = 0 (required for EPC scan) / DirectMode = 1 (for direct carrier)
    [Status, ResultFlag] = invoke(kathreinReader, 'SetFrequency', 868);  % 865.7 MHz wurde zu 868 geändert
    [Status, ResultFlag] = invoke(kathreinReader, 'SetAntenna', 2);        % AntennaPort 1
    [Status, ResultFlag, AntennenPort] = invoke(kathreinReader, 'SetPortPower', 2, power_dbm*4); % (x/4)dBm = Sendeleistung an Port 1

    return_dat = kathreinReader;

    
%% ResultFlag-Meaning:
% 0               NoError
% 1               NoData
% 2               CRCError
% 3               NoLicense
% 4               OutOfRange
% 5               NoStandard
% 6               NoAntenna
% 7               NoFrequency
% 8               NoCarrier
% 9               AntennaError
% 10              NoTag
% 11              MoreThanOneTagInField
% 12              WrongLicenseKey
% 13              FWRejected
% 14              WrongCFM
% 15              NoHandle
% 16              NoProfile  
% 128             NonSpecified






