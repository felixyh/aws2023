from Scripts.ctf_0_basic_functions import create_update_stack

if __name__ == "__main__":
    template_path = "../../AWS_1_EC2/ec2_0_vpc.yaml"
    stack_name = 'FelixEC2VPC'
    print(create_update_stack(stack_name, template_path))