import nglview as nv
from ase import Atoms
from ase.io.trajectory import TrajectoryReader

def view_ngl(atoms, showindex=False, showcell=True):
    """
    Display an interactive visualization of atoms using nglview.

    Args:
        atoms (ase.Atoms): The ASE atoms object to visualize.
        showindex (bool, optional): If True, display indices next to atoms. Default is False.
        showcell (bool, optional): If True, display the unit cell. Default is True.

    Returns:
        nglview.NGLWidget: An NGLWidget instance for the provided atomic structure.
    """
    # nglview settings
    if isinstance(atoms, Atoms): # atoms
        view = nv.show_ase(atoms)

    elif isinstance(atoms, TrajectoryReader): # ase trajectory
        view = nv.show_asetraj(atoms, gui=True)


    if showindex == True: # show atomindex
        view.add_label(labelType="text", labelText=[f"{atom.symbol}_{i}" for i, atom in enumerate(atoms)], color='black')

    if showcell == True: # show unit cell
        view.add_unitcell()

    return view