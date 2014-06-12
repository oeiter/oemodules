openerp.simpleblog = function (instance) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;
    
    instance.web.simpleblog = instance.web.simpleblog || {};
    
    instance.web.client_actions.add('simpleblogtag', 'instance.web.simpleblog.blogtag');
    instance.web.simpleblog.blogtag = instance.web.Widget.extend({
    	template: "SimpleblogTemplate",  
    	
        init: function(parent, context) {
            this._super(parent);
        },
    
        start: function() {
            this._super();
            var self = this;
            self.$el.find("button.simplesave").click(function() {
                self.btn_clicked();
            });
            self.$el.find("input.simple_name").change(function() {
                self.input_change();
            });
        },
        input_change: function() {
        	 var blogmodel =new instance.web.Model("simpleblog.blogdetails");
             blogmodel.call('get_blog_from_details', [[]]).then(function (result){ 
             	alert(result);
             });
        },
        btn_clicked: function() {
            this.do_action({
                type: 'ir.actions.act_window',
                res_model: "simpleblog.category",
                res_id: 1,
                views: [[false, 'form']],
                target: 'new',
                context: {},
            });
        },
    });
};
