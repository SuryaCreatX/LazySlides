import aspose.slides as slides
import glob

# Create presentation
class pdfin:
    def __init__(self,make):
        self.make = make
        with slides.Presentation() as pres:

            # Remove default slide from presentation
            pres.slides.remove_at(0)

            # Import PDF to presentation
            for path in glob.glob("pdfin/*.pdf"):
                pres.slides.add_from_pdf(path)

            # Save presentation
            pres.save("pdf-to-ppt.pptx", slides.export.SaveFormat.PPTX) 