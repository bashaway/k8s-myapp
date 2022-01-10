const base_url=location.protocol+"//"+location.host+"/api/fastapiapp";

function buildUrl (url) {
  return base_url + url;
}


function parseQueryString(str) {

    let objURL = {};
    str.replace(
        new RegExp( "([^?=&]+)(=([^&]*))?", "g" ),
        function( $0, $1, $2, $3 ){
            objURL[ $1 ] = $3;
        }
    );
    return objURL;
};



const tableAppVM = Vue.createApp({
  data() {
    let queryParams = parseQueryString(location.search);

    return {
      records: [],
      tables: [],
      create_inputs: {},
      search_inputs: {},
      table_columns: [],
      result: '',
      record_count: '',
      all_pages: '',
      primary_key: '',
      default_table: 'users',
      default_limit: '10',
      selectable_limits: ['10','20','50','100'],
      current_table: queryParams['table'],
      current_limit: queryParams['limit'],
      current_page:  queryParams['page'],
    }
  },

  mounted () {
    let queryParams = parseQueryString(location.search);
    let search_param = '';
    let flg_reload = false;

    if( queryParams['table'] ){
        search_param += '?table='+queryParams['table'];
    }else{
        //console.log('TABLE DEFAULT');
        search_param += '?table='+this.default_table;
        flg_reload = true;
    }

    if( (queryParams['limit'])  && (this.selectable_limits.includes(queryParams['limit']))){
        search_param += '&limit='+queryParams['limit'];
    }else{
        //console.log('LIMIT DEFAULT');
        search_param += '&limit='+this.default_limit;
        flg_reload = true;
    }

    if( (queryParams['page']) && (queryParams['page'] >= 1)){
        search_param += '&page='+queryParams['page'];
    }else{
        //console.log('PAGE DEFAULT');
        search_param += '&page=1';
        flg_reload = true;
    }

    // パラメータが不十分な場合はリロードする
    if ( flg_reload ) {
        //console.log('RELOAD: '+search_param);
        location.search=search_param;
    }else{
        this.getRecordCount();
        this.getAllRecords();
        this.getTableColumns();
        this.getTables();
    }


  },

  watch: {
    current_table: function(next, prev) {
      //console.log('表示テーブル変更:'+prev+'->'+next);
      location.search = "?table="+next+"&limit="+this.current_limit+"&page=1";
    },

    current_limit: function(next, prev) {
      //console.log('表示件数変更:'+prev+'->'+next);
      location.search = "?table="+this.current_table+"&limit="+next+"&page=1";
    },

    current_page: function(next, prev) {
      //console.log('表示ページ変更:'+prev+'->'+next);
      location.search = "?table="+this.current_table+"&limit="+this.current_limit+"&page="+next;
    },


    search_inputs: {
      handler: function(next, prev){
        let query='';
        Object.keys(next).forEach(key => query=query+'&'+key+'='+next[key] );

        this.getRecordCount(query);
        this.getAllRecords(query);

        //console.log(query);
      },
      deep: true
    },


  },

  methods: {

    clear_search_inputs(){
      this.search_inputs={};
      this.current_page=1;
      this.current_limit=this.default_limit;
    },


    getTables: function() {
      let tablePath = '/';
      let url = buildUrl(tablePath);

      axios.get(url)
         .then( response => {
           this.tables = response.data;
           //console.log(response.data);
         })
         .catch( error => {
           console.log(error);
         });

    },


    getTableColumns: function() {
      let tablePath = '/'+this.current_table+'/meta';
      let url = buildUrl(tablePath);

      axios.get(url)
         .then( response => {
           this.table_columns = response.data;
           //console.table(response.data);
           for( column of response.data ){
             if( column.column_primary_key ){
               this.primary_key = column.column_name;
             }
           }
           //console.log(this.primary_key);
         })
         .catch( error => {
           console.log(error);
         });

    },

    getRecordCount: _.debounce(function(query='') {
      let tablePath = '/'+this.current_table+'/count?';
      let url = buildUrl(tablePath);

      if(query){ url = url+query; }

      axios.get(url)
         .then( response => {
           this.record_count = response.data.count;
           this.all_pages=Math.ceil(this.record_count / this.current_limit);
           //if(this.all_pages < this.current_page ){ this.current_page = 1; }
         })
         .catch( error => {
           console.log(error);
         });
    },300),


    getAllRecords: _.debounce(function(query='') {
      let tablePath = '/'+this.current_table
                     +'/?limit='+this.current_limit
                     +'&skip='+(this.current_limit*(this.current_page-1));
      let url = buildUrl(tablePath);

      if(query){ url = url+query; }

      axios.get(url)
         .then( response => {
           this.records = response.data;
           //console.log(tablePath);
           //console.log(response.data[0]);
         })
         .catch( error => {
           console.log(error);
         })
    },300),


    read_one(record) {
      let tablePath = '/'+this.current_table+'/';
      let url = buildUrl(tablePath+record[this.primary_key]);
      axios.get(url)
        .then( response => {
            this.result = response.data;
            this.result.msg = "詳細取得";
            //console.log(response);
        })
        .catch( error => {
            this.result = error;
            this.result.msg = "詳細取得エラー";
            console.table(record);
            console.log(error);
        });
    },


    create_one() {
      let tablePath = '/'+this.current_table+'/';
      let url = buildUrl(tablePath);

      axios.post(url, this.create_inputs)
        .then( response => {
            this.records.push(response.data);
            this.result = response.data;
            this.result.msg = "新規登録しました";
            this.create_inputs = {};
            this.getRecordCount();
            //console.log(response);
        })
        .catch( error => {
            this.result = error;
            this.result.msg = "登録エラー";
            console.log(error);
        })
    },

 
    update_one(record) {
      let tablePath = '/'+this.current_table+'/';
      let url = buildUrl(tablePath+record[this.primary_key]);

      // 更新された値が空欄である場合
      // カラムがnullableならnullにしてAPIへ投げる
      for( cname of this.table_columns ){
        if( (record[cname.column_name]=='') && (cname.column_nullable) ){
          record[cname.column_name]=null
          console.table(record);
        }
      }

      axios.patch(url, record)
        .then( response => {
            this.result = response.data;
            this.result.msg = "更新しました";
            //console.log(response);
        })
        .catch( error => {
            this.result = error;
            this.result.msg = "更新エラー";
            console.log(error);
        })
    },

    delete_one(record,index) {
      let tablePath = '/'+this.current_table+'/';
      let url = buildUrl(tablePath+record[this.primary_key]);
      axios.delete(url)
        .then( response => {
            this.result = response.data;
            this.result.msg = "削除しました";
            this.records.splice(index,1)
            this.getRecordCount();
            //console.log(response);
        })
        .catch( error => {
            this.result = error;
            this.result.msg = "削除エラー";
            console.log(error);
        })
    },


  }
});

tableAppVM.mount('#table-app');
