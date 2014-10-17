window.$_BBQ = {
    sw: 1,
    request: function(action, params, callback){
        if (!params) params = [];
        this.callback = callback;
        window.location = '#BBQ' + this.sw + '::' + action + '|' + JSON.encode(params);
        this.sw = (this.sw == 1 ? 2 : 1);
    },

    execute_callback: function(content){
        content = decodeURIComponent(content);
        this.callback(content);
    }
};

window.Barbacoa = {

    version: 0.1,

    plugins: [],

    File: {
        write: function(filename, content) {
            $_BBQ.request('File.write', [filename, content]);
        },
        choose_directory: function(selected_dir, callback) {
            $_BBQ.request('File.choose_directory', [selected_dir], callback);
        }
    },

    Environment: {
        get_user_home: function(callback){
            $_BBQ.request('Environment.get_user_home', [], callback);
        }

    }

};

$_BBQ.request('load-plugins');
if (typeof(BarbacoaReady) == 'function'){
    BarbacoaReady();
}