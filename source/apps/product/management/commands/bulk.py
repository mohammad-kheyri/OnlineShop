import random
from pathlib import Path
from django.core.management.base import BaseCommand
from django.core.files import File
from apps.product.models import Product, Color, ProductCategory, Brand  # ✅ import related models


class Command(BaseCommand):
    help = "Creates 100 random shoe products with valid foreign key relationships"

    def handle(self, *args, **options):
        # ---- Seed Data ----
        different_names = [
            "addidas New Hammer sole for Sports person",
            "Men’s Waterproof Garden Shoes Rain Boots Slip-On Footwear",
            "THESTRON Men Golf Shoes Mesh Breathable Breathable Golf Walking",
            "Water Shoes Wide Width for Women Men Swim Beach Barefoot Shoes",
            "Steel Toe Shoes for Men Comfortable Indestructible Safety Work Boots for Men",
            "HOKA Men's Bondi 9 Sneaker"
        ]

        color_names = ["black", "white", "red", "yellow", "orange"]
        category_names = ["boots", "boat shoes", "comfort shoes", "hiking shoes", "sports"]
        brand_names = ["addidas", "brooks", "nike", "puma"]

        original_price_range = range(150, 200)
        off_price_range = range(100, 149)
        availability = range(10, 30)

        base_dir = Path(__file__).resolve().parent.parent.parent.parent.parent  # up to project root
        img_path = base_dir / "static/img/product"
        print(base_dir)


        description = """
        Mill Oil is an innovative oil filled radiator with the most modern technology.
        If you are looking for something that can make your interior look awesome,
        and at the same time give you the pleasant warm feeling during the winter.
        """

        # ---- Ensure Foreign Keys Exist ----
        colors = [Color.objects.get_or_create(name=name)[0] for name in color_names]
        categories = [ProductCategory.objects.get_or_create(name=name)[0] for name in category_names]
        brands = [Brand.objects.get_or_create(name=name)[0] for name in brand_names]

        self.stdout.write(self.style.SUCCESS("✅ Ensured all Color, Category, and Brand entries exist."))

        # ---- Collect Images ----
        image_files = list(img_path.glob("*.jpg")) + list(img_path.glob("*.png"))
        if not image_files:
            self.stdout.write(self.style.WARNING("⚠️ No images found in static/img/product/"))
        products = Product.objects.all()

        # ---- Create Products ----
        for product in products:
            

            # Attach random image (optional)
            if image_files:
                image_file = random.choice(image_files)
                with open(image_file, "rb") as f:
                    product.image.save(image_file.name, File(f), save=True)
                    print(image_file.name)

            # self.stdout.write(self.style.SUCCESS(f"🆕 Created product {i+1}: {product.name}"))

        self.stdout.write(self.style.SUCCESS("🎉 100 products created successfully!"))
