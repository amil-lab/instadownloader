import instaloader
import os
import time
from urllib.parse import urlparse

def extract_shortcode_from_url(url):
    """Extract the Instagram post shortcode from URL"""
    path = urlparse(url).path
    # Remove trailing slash if present
    path = path.rstrip('/')
    # Get the last component of the path
    return path.split('/')[-1]

def download_instagram_post(url, output_path="downloads"):
    try:
        # ==============================
        # 1. SETUP & CONFIGURATION
        # ==============================
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Initialize Instaloader instance
        L = instaloader.Instaloader(
            download_pictures=True,
            download_videos=True,
            download_video_thumbnails=False,
            download_geotags=False,
            download_comments=False,
            save_metadata=False,
            post_metadata_txt_pattern=''
        )

        # ==============================
        # 2. EXTRACT POST ID & DOWNLOAD
        # ==============================
        print(f"\n📥 Processing Instagram URL: {url}")
        shortcode = extract_shortcode_from_url(url)
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        print(f"📝 Post description: {post.caption[:100]}..." if post.caption else "No caption")
        print(f"📂 Output Path: {os.path.abspath(output_path)}")

        # Start download
        start_time = time.time()
        
        # Change working directory temporarily
        original_dir = os.getcwd()
        os.chdir(output_path)
        
        print("\n⏳ Downloading media...")
        L.download_post(post, target=shortcode)

        # Restore working directory
        os.chdir(original_dir)

        # ==============================
        # 3. FINAL VALIDATION
        # ==============================
        download_time = time.time() - start_time
        
        print("\n✅ Download completed successfully!")
        print(f"⏱️ Time taken: {download_time:.2f} seconds")
        print(f"💾 Saved to: {os.path.join(os.path.abspath(output_path), shortcode)}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    # ==============================
    # EXAMPLE USAGE
    # ==============================
    print("Instagram Media Downloader")
    print("-------------------------")
    instagram_url = input("Enter Instagram post URL: ").strip()
    
    download_instagram_post(
        instagram_url,
        output_path="downloads"
    )
