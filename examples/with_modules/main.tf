module "test_module" {
  source = "./some_module"
  test_var = "var"
}

output "test_string_from_root" {
  value = "hello_from_root"
}
