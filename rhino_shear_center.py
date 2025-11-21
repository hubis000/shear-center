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

# %%
# Load a geometry with a single region from a dxf file

# %%
# Load a geometry from a 3dm (Rhino) file
file_names=[i for i in os.listdir(os.curdir) if i.endswith('.3dm')]
geom = Geometry.from_3dm(filepath=file_names[0])
geom.plot_geometry()

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


