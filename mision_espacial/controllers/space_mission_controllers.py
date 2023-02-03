from odoo import http

class SpaceMission(http.Controller):
    @http.route('/mision_espacial/', auth='public', website=True, sitemap=True)
    def index(self,**kw):
        return "Welcome to the Top Secret Space Mission!"
    
    @http.route('/mision_espacial/missions/', auth='public', website=True, sitemap=False)
    def missions(self,**kw):
        missions = http.request.env['mision_espacial.mission'].search([])
        return http.request.render('mision_espacial.mission_website',{
            'missions': missions,
        })