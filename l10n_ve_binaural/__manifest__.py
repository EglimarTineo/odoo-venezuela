# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Venezuela - Binaural",
    "version": "1.0",
    "category": "Accounting/Localizations/Account Charts",
    "summary": "Localización Contable para Venezuela (Plan de Cuentas e Impuestos)",
    "website": "https://shopink.com.ve",
    "author": "Odoo S.A., Binaural C.A",
    "countries": ["ve"],
    "depends": [
        "account",
        "base_vat",
    ],
    "data": [
        "data/template/account.tax.group-ve.csv",
        "data/template/account.account-ve.csv",
        "data/template/account.tax-ve.csv",
    ],
    "demo": [
        "demo/demo_company.xml",
    ],
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
