variable "test_var" {}

output "test_var" {
  value = "${var.test_var}"
}

output "test_string_from_module" {
  value = "hello_from_module"
}
