/** @odoo-module **/

import Chrome from "point_of_sale.Chrome"; 
const Registries = require('point_of_sale.Registries'); 

const ThemeBitsChrome = (Chrome) =>
    class extends Chrome {
        async start(){ 
            try { 
                await super.start(...arguments)
            
                var theme_configuration_id = this.env.pos.config.theme_configuration_id ? this.env.pos.config.theme_configuration_id[0] : undefined; 
                if(theme_configuration_id){
                    this.theme_config_bits = await this.get_theme_config(theme_configuration_id);
                }
                // console.log(this.theme_config_bits[0].theme_active, "estamos aca");
                if(this.theme_config_bits && this.theme_config_bits[0].theme_active){
                    document.documentElement.style.setProperty("--theme_primary_color", this.theme_config_bits[0].theme_primary_color); 
                    document.documentElement.style.setProperty("--theme_secondary_color", this.theme_config_bits[0].theme_secondary_color); 
                }else{
                    document.documentElement.style.setProperty("--theme_primary_color",'#714B67');
                    document.documentElement.style.setProperty("--theme_secondary_color",'#017e84');
                }   
            }catch(error) {
                this.env._t( error);
            }
            const height = $(window).height();
            $('.pos').css('height',height+'px'); 
            $(window).resize(function(){
                const height = $(window).height();
                $('.pos').css('height',height+'px');
            }); 
        }
        ToggleMenu(ev) { 
            var target = $(ev.target).parents('.pos').find('.pos-topheader')
            target.toggleClass('lb_visible');
            target.toggleClass('left');
        } 
        onLeave(ev){
            var link_btns = $(ev.currentTarget).find('.link-btn-text')
            if(link_btns[0].classList.contains('hide')){
                link_btns.toggleClass('hide');
            }
            $(ev.currentTarget).removeClass('lb_visible');
        }
        async get_theme_config(theme_configuration_id){ 
            return await this.rpc({
                model: 'pos.theme.config',
                method: 'search_read',
                args: [[['id', 'in', [theme_configuration_id]]]],
            })
        }
    };
Registries.Component.extend(Chrome, ThemeBitsChrome);  