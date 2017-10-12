from io import StringIO, BytesIO
from xhtml2pdf import pisa

from django.template.loader import get_template


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(
        StringIO(html),
        dest=result,
        encoding='UTF-8'
    )

    return pdf, result
