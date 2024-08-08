/** @odoo-module */
 
import { ChromeAdapter } from "@point_of_sale/entry/chrome_adapter";
import { patch } from "@web/core/utils/patch";  
const { useSubEnv } = owl;

patch(ChromeAdapter.prototype,'point_of_sale/entry/chrome_adapter',{
    setup(){
        this._super();
        useSubEnv({
            get isMobile() { 
                return window.innerWidth <= 991;
            },
        });
    }
});
