import json
import numpy as np

def pixel_to_world(column, row, slice_nr, origin, spacing, direction_matrix): 
    # order in world coordinates is: column, row, slice in RAI coordinate
    # system (ITK default) also known as DICOM LPS or Nrrd
    # RAI means:
    # X: patient Right to left
    # Y: patient Anterior to posterior
    # Z: patient Inferior to superior

    world_coordinates = (np.array([column, row, slice_nr]) * spacing) @ direction_matrix + origin
    return world_coordinates


def world_to_pixel(world_coordinates, origin, spacing, direction_matrix):
    # column, row, index (slice number)
    cri = ((world_coordinates - origin) @ np.linalg.inv(direction_matrix)) / spacing    
    
    cri = np.round(cri).astype(int)
    slice_nr = cri[2]
    pixel_coordinates = cri[0:2]
    return pixel_coordinates, slice_nr




def load_h5_file(filepath):
    # loads an hdf5 file and returns the image and mask datasets
    import h5py

    with h5py.File(filepath, 'r') as f:
        print(list(f.keys()))
        image = f['images'][:]
        mask = f['masks'][:]

        metadata_str = f['metadata'][:]
        metadata = []
        for m in metadata_str:
            metadata.append(json.loads(m))
    return image, mask, metadata
