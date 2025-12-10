from luna16_helpers import load_h5_file
import matplotlib.pyplot as plt


filename = r"P:\mmunz\Lehre\IAML\LUNA16\extracted\bin\1\1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860_1.h5"

# Example usage
image, mask, metadata = load_h5_file(filename)


print(f"Image shape: {image.shape}")
print(f"Mask shape: {mask.shape}")
print(f"Number of candidates in this file: {len(metadata)}")


candidate_nr = 0

# output the metadata for the candidate
print(f"Metadata for candidate {candidate_nr}: {metadata[candidate_nr]}")

# example access to metadata fields
uid = metadata[candidate_nr]['uid']
class_label = metadata[candidate_nr]['label']


# Display a candidate patch and its binary mask
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(image[candidate_nr, :, :], cmap='gray')
plt.title('Image patch, class='+str(class_label))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(mask[candidate_nr, :, :], cmap='gray')
plt.title('Mask patch, class='+str(class_label))
plt.axis('off')

plt.show()