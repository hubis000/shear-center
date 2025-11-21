r"""
.. _ref_cad_import:

Importing Geometry from CAD
---------------------------

Demonstrates loading :class:`~sectionproperties.pre.geometry.Geometry` and
:class:`~sectionproperties.pre.geometry.CompoundGeometry` objects from `.dxf` and `.3dm` (Rhino)
files.
"""

# sphinx_gallery_thumbnail_number = 8

from sectionproperties.pre.geometry import Geometry, CompoundGeometry
from sectionproperties.analysis.section import Section
import os
import tkinter as tk
from tkinter import filedialog  
from tkinter import scrolledtext 
from antfunctions import antfunctions
# %%
# Load a geometry with a single region from a dxf file

# %%
# Load a geometry from a 3dm (Rhino) file
# Define file path with tkinter
root = tk.Tk()
root.withdraw()  # Hide the root window
file_names = filedialog.askopenfilenames(title="Select 3dm file", filetypes=[("3dm files", "*.3dm")])
# Get the directory from the selected file path
folder_path = os.path.dirname(file_names[0])
# Load geometry
geom = Geometry.from_3dm(filepath=file_names[0])
geom.plot_geometry()
root.destroy()

# %%
# Generate a mesh
geom.create_mesh([1])
sec = Section(geom)
sec.plot_mesh(materials=False)

# %%
# Conduct a geometric & plastic analysis
sec.calculate_geometric_properties()
sec.calculate_plastic_properties()
sec.calculate_warping_properties()
(x_se, y_se) = sec.get_sc()
(x11_se, y22_se) = sec.get_sc_p()
(x_st, y_st) = sec.get_sc_t()

print("Centroidal axis shear centre (elasticity approach) (x_se, y_se)",x_se, y_se)
print("Principal axis shear centre (elasticity approach) (x11_se, y22_se)",x11_se, y22_se)
print("Centroidal axis shear centre (Trefftz’s approach) (x_st, y_st)",x_st, y_st)
sec.plot_centroids()


# %%
# Display the geometric & plastic properties
sec.display_results()
#tkinter print results in a scrollable text box
# display simple box with restults without using tkinter console
results = "Centroidal axis shear centre (elasticity approach) (x_se, y_se)\n",x_se, y_se
# results += "\nPrincipal axis shear centre (elasticity approach) (x11_se, y22_se)\n",x11_se, y22_se
# results += "\nCentroidal axis shear centre (Trefftz’s approach) (x_st, y_st)\n",x_st, y_st
root = tk.Tk()
root.title("Section Properties Results")        
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
text_area.insert(tk.END, results)
text_area.configure(state='disabled')  # Make the text area read-only
root.mainloop()


antfunctions.script_version(folder_path)