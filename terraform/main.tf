resource "google_storage_bucket" "raw_landing" {
  name     = var.bucket_name
  location = "ASIA"

  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  public_access_prevention = "enforced"

  force_destroy = false
}
resource "google_bigquery_dataset" "staging" {
  dataset_id = "d1_staged"
  location   = var.region

  delete_contents_on_destroy = false
}
resource "google_storage_bucket_iam_member" "viewer" {
  bucket = google_storage_bucket.raw_landing.name
  role   = "roles/storage.objectViewer"
  member = "user:amrutasuryavanshi212@gmail.com"
