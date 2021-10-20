function return_dat = reader_disconnect(obj)
    if ~isempty(obj)
        if isvalid(obj)
            disconnect(obj);
            delete(obj);
            return_dat = 'connection successfully closed.';
        end
        clear kathreinReader;
    end