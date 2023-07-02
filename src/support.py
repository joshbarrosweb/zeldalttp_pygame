import pygame
from csv import reader
from os import walk

# Function to import a CSV layout file and convert it into a 2D list
def import_csv_layout(path):
  terrain_map = []
  with open(path) as level_map:
    layout = reader(level_map, delimiter = ',')
    for row in layout:
      terrain_map.append(list(row))
    return terrain_map

# Function to import all images from a given folder into a list of pygame surfaces
def import_folder(path):
  surface_list = []

  # Loop through the provided directory and add each image file to the surface list
  for _, _, img_files  in walk(path):
    for image in img_files:
      full_path = path + '/' + image

      # Load the image and convert it to a format pygame can easily work with
      image_surf = pygame.image.load(full_path).convert_alpha()

      # Append the image surface to the list
      surface_list.append(image_surf)
    return surface_list
