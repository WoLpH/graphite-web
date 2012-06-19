var MetricCompleter;

MetricCompleter = Ext.extend(Ext.form.TextArea, {
    displayField: 'path',
    listEmptyText: 'No matching metrics',
    mode: 'remote',
    hideTrigger: true,
    queryDelay: 100,
    queryParam: 'query',
    typeAhead: false,
    minChars: 1,

    initComponent: function () {
        var _this = this;

        var store = new Ext.data.JsonStore({
        url: '../metrics/find/',
        root: 'metrics',
        fields: ['path', 'name'],
        baseParams: {format: 'completer'}
        });

        var config = {store: store};

        Ext.apply(this, config);
        Ext.apply(this.initialConfig, config);

        MetricCompleter.superclass.initComponent.call(this);

        this.addListener('beforequery', this.prepareQuery.createDelegate(this));
        this.addListener('specialkey', this.onSpecialKey.createDelegate(this));
        this.addListener('afterrender',
        function () {
            _this.getEl().addListener('specialkey',
            function (el, e) {
                _this.onSpecialKey(_this.getEl(), e);
            }
            );
        }
        );
    },

    prepareQuery: function (queryEvent) {
        queryEvent.query += '*';
    },

    onSpecialKey: function (field, e) {
        var key = e.getKey();
        if(key == e.TAB){
            /* allow the user to insert tabs */
            var el = field.el.dom;
            var startPos = el.selectionStart;
            var endPos = el.selectionEnd;
            var value = field.getValue();
            field.setValue(
                value.substring(0, el.selectionStart)
                + '  '
                + value.substring(el.selectionEnd, value.length)
            );
            el.setSelectionRange(startPos + 2, endPos + 2);
            e.stopEvent();
            return false;
        }else if(key == e.ENTER){
            var value = field.getValue();
            braces = value.match(/\(/g).length - value.match(/\)/g).length;
            field.setValue(
                value
                + '\n'
                + Array(braces + 1).join('  ')
            );
            e.stopEvent();
            return false;
        }
    }
});

Ext.reg('metriccompleter', MetricCompleter);
