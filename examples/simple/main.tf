variable "list_var" {
  type = "list"
  default = [1,2,3]
}

variable "string_var" {
  type = "string"
  default = "hello"
}

output "test_string" {
  value = "${var.string_var}"
}

output "test_list" {
  value = "${var.list_var}"
}
