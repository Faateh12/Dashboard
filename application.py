from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
import jwt

application = Flask(__name__, template_folder="Templates")
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Faateh:Faateh123@dashboard-db.cwvdgyt4btit.us-east-1.rds.amazonaws.com:5432/dashboard_db'
application.config['SECRET_KEY'] = 'secret!'
application.config['SQLALCHEMY_BINDS'] = {
    'database1': 'postgresql://Faateh:Faateh123@rma-tool-db.cwvdgyt4btit.us-east-1.rds.amazonaws.com:5432/rma_tool_db',
    'database2': 'postgresql://postgres:test1234@test-db.cwvdgyt4btit.us-east-1.rds.amazonaws.com:5432/test_db',
    'database3': 'postgresql://Faateh:Faateh123@trials-db.cwvdgyt4btit.us-east-1.rds.amazonaws.com:5432/test_db',
    'database4': 'postgresql://Faateh:Faateh123@projects-db.cwvdgyt4btit.us-east-1.rds.amazonaws.com:5432/projecttool_db'
}
db = SQLAlchemy(application)
login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

class RmaTool(db.Model):
    __bind_key__ = 'database1'
    __tablename__ = 'rma_test'
    # Define your model fields and relationships
    MAT_RMA_ID = db.Column(db.String(100), primary_key=True)
    DATE_RMA_RECEIVED = db.Column(db.String(50), nullable=False)
    CUSTOMER_OPERATOR = db.Column(db.String(1000), nullable=False)
    SUBCONTRACTOR = db.Column(db.String(1000), nullable=True)
    MATSING_REP = db.Column(db.String(50), nullable=True)
    ANTENNA_MODEL_NO_SERIAL_NO = db.Column(db.String(200), nullable=False)
    STATUS = db.Column(db.String(50), nullable=True)
    ISSUE = db.Column(db.String(500), nullable=True)
    RESOLUTION = db.Column(db.String(1000), nullable=True)
    DATE_RESOLVED = db.Column(db.String(25), nullable=True)
    DEFECTIVE_UNITS_LOCATION_INFO = db.Column(db.String(200), nullable=True)
    NEXT_STEPS = db.Column(db.String(200), nullable=True)
    requestor_company_name = db.Column(db.String(255), nullable=True)
    requestor_contact_name = db.Column(db.String(255), nullable=True)
    requestor_email_address = db.Column(db.String(255), nullable=True)
    requestor_phone_number = db.Column(db.String(255), nullable=True)
    requestor_role = db.Column(db.String(255), nullable=True)
    original_po_number = db.Column(db.String(255), nullable=True)
    model_numbers_of_antennas_being_returned = db.Column(db.String(255), nullable=True)
    serial_numbers_of_antennas_being_returned = db.Column(db.String(255), nullable=True)
    problem_description = db.Column(db.String(5000), nullable=True)
    replacement_shipment_contact_name = db.Column(db.String(255), nullable=True)
    replacement_shipment_contact_phone_number = db.Column(db.String(255), nullable=True)
    replacement_shipment_email_address = db.Column(db.String(255), nullable=True)
    replacement_shipment_receiving_location = db.Column(db.String(255), nullable=True)
    replacement_shipment_instructions = db.Column(db.String(255), nullable=True)
    company = db.Column(db.String(255), nullable=True)
    contact_person_for_pick_up = db.Column(db.String(255), nullable=True)
    pick_up_location_of_antenna_to_be_returned = db.Column(db.String(255), nullable=True)
    contact_email_for_pick_up = db.Column(db.String(255), nullable=True)
    contact_phone_number_for_pick_up = db.Column(db.String(255), nullable=True)
    date_ready_for_pick_up = db.Column(db.String(255), nullable=True)
    wireless_operator_company_name = db.Column(db.String(255), nullable=True)
    wireless_operator_contact_name = db.Column(db.String(255), nullable=True)
    wireless_operator_email_address = db.Column(db.String(255), nullable=True)
    wireless_operator_phone_number = db.Column(db.String(255), nullable=True)
    matsing_rep_company_name = db.Column(db.String(255), nullable=True)
    matsing_rep_contact_name = db.Column(db.String(255), nullable=True)
    matsing_rep_email_address = db.Column(db.String(255), nullable=True)
    matsing_rep_phone_number = db.Column(db.String(255), nullable=True)
    is_this_a_new_issue = db.Column(db.String(255), nullable=True)
    is_this_an_event_site = db.Column(db.String(255), nullable=True)
    is_this_a_macro_site = db.Column(db.String(255), nullable=True)
    image = db.Column(db.LargeBinary, nullable=True)
    image_2 = db.Column(db.LargeBinary, nullable=True)
    image_3 = db.Column(db.LargeBinary, nullable=True)
    user = db.Column(db.String(25), nullable=True)
    unique_key = db.Column(db.String(50), nullable=True)
    order_no = db.Column(db.String(25), nullable=True)
    date_updated = db.Column(db.String(25), nullable=True)
    days_since_rma = db.Column(db.String(10), nullable=True)
    summary_status = db.Column(db.String(200), nullable=True)
    open_closed = db.Column(db.String(25), nullable=True)
    rma_summary_issue = db.Column(db.String(50), nullable=True)
    rma_summary_country = db.Column(db.String(50), nullable=True)
    rma_summary_city = db.Column(db.String(50), nullable=True)
    rma_summary_field_engineer = db.Column(db.String(50), nullable=True)
    filename_1 = db.Column(db.String(1000), nullable=True)
    filename_2 = db.Column(db.String(1000), nullable=True)
    filename_3 = db.Column(db.String(1000), nullable=True)
    s3url1 = db.Column(db.String(300), nullable=True)
    s3url2 = db.Column(db.String(300), nullable=True)
    s3url3 = db.Column(db.String(300), nullable=True)
    priority = db.Column(db.String(200), nullable=True)
    deadline = db.Column(db.String(200), nullable=True)
    assigned_to = db.Column(db.String(50), nullable=True)
    parts_ordered = db.Column(db.String(500), nullable=True)
    parts_required = db.Column(db.String(500), nullable=True)
    parts_delivery_eat = db.Column(db.String(500), nullable=True)
    site_name = db.Column(db.String(255), nullable=True)
    summary_model_no = db.Column(db.String(1000), nullable=True)
    summary_serial_no = db.Column(db.String(1000), nullable=True)
    replacement_unit_delivered_date = db.Column(db.String(100), nullable=True)
    defective_unit_returned_date = db.Column(db.String(100), nullable=True)
    inspection_report_status = db.Column(db.String(100), nullable=True)
    queue = db.Column(db.String(100), nullable=True)
    qc_report_status = db.Column(db.String(255), nullable=True)
    under_warranty = db.Column(db.String(255), nullable=True)
    rep_firm = db.Column(db.String(100), nullable=True)
    site_name_form = db.Column(db.String(255), nullable=True)
    is_there_physical_damage = db.Column(db.String(25), nullable=True)
    radio_vender = db.Column(db.String(255), nullable=True)
    radio_model_number = db.Column(db.String(255), nullable=True)
    new_repeat = db.Column(db.String(255), nullable=True)
    replacement_unit_model_no = db.Column(db.String(500), nullable=True)

class TechSupport(db.Model):
    __bind_key__ = 'database2'
    # Define your model fields and relationships
    __tablename__ = 'Ticket'
    ticket_id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    email = db.Column(db.String(100))
    subject = db.Column(db.String(50))
    issue = db.Column(db.String(5000))
    date_submitted = db.Column(db.String(50))
    company_name = db.Column(db.String(255))
    antenna_model_number = db.Column(db.String(255))
    status = db.Column(db.String(255))
    resolution_date = db.Column(db.String(255))
    resolution_eta = db.Column(db.String(255))
    Priority = db.Column(db.String(255))
    ticket_year = db.Column(db.String(100))
    open_closed = db.Column(db.String(255))

class Trials(db.Model):
    __bind_key__ = 'database3'
    # Define your model fields and relationships
    __tablename__ = 'trials'
    trial_id = db.Column(db.String(50), primary_key=True)
    trial_year = db.Column(db.String(50))
    country = db.Column(db.String(50))
    operator = db.Column(db.String(255))
    rep_company = db.Column(db.String(255))
    venue = db.Column(db.String(255))
    status = db.Column(db.String(255))
    start_date = db.Column(db.String(50))
    end_date = db.Column(db.String(50))
    result = db.Column(db.String(500))
    antenna_status = db.Column(db.String(255))
    notes = db.Column(db.String(1000))
    last_updated = db.Column(db.String(500))
    antenna_readiness_eta = db.Column(db.String(255))
    antenna_shipment_eta = db.Column(db.String(255))
    aos_status = db.Column(db.String(500))
    model_qty = db.Column(db.String(500))
    shipped_model_serial = db.Column(db.String(500))

class Projects(db.Model):
    __bind_key__ = 'database4'
    # Define your model fields and relationships
    __tablename__ = 'projects'
    project_id = db.Column(db.String(50), primary_key=True)
    project_year = db.Column(db.String(50))
    country = db.Column(db.String(50))
    status = db.Column(db.String(255))
    start_date = db.Column(db.String(50))
    end_date = db.Column(db.String(50))
    result = db.Column(db.String(500))
    notes = db.Column(db.String(1000))
    last_updated = db.Column(db.String(500))

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(300))
    password = db.Column(db.String(300))
    name = db.Column(db.String(300))


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

def generate_token(user_email):
    # Generate a JWT token
    payload = {'user_email': user_email}
    token = jwt.encode(payload, 'secret_key', algorithm='HS256')
    return token

@application.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('login'))


@application.route('/rma-login')
def app_login_rma():
    current = current_user._get_current_object()
    email = current.email
    token = generate_token(user_email=email)
    link = f'https://matsing-rmaplatform.com/login?token={token}'
    return redirect(link)

@application.route('/techsupport-login')
def app_login_techsupport():
    current = current_user._get_current_object()
    email = current.email
    token = generate_token(user_email=email)
    link = f'https://matsing-techsupport.com/?token={token}'
    return redirect(link)

@application.route('/trials-login')
def app_login_trials():
    current = current_user._get_current_object()
    email = current.email
    token = generate_token(user_email=email)
    link = f'https://matsing-trials.com/?token={token}'
    return redirect(link)

@application.route('/projects-login')
def app_login_projects():
    current = current_user._get_current_object()
    email = current.email
    token = generate_token(user_email=email)
    link = f'https://matsing-projects.com/?token={token}'
    return redirect(link)



@application.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'loginEmail' in request.form and 'loginPassword' in request.form:
            # Login request
            login_email = request.form.get('loginEmail')
            login_password = request.form.get('loginPassword')

            # Process login data here (e.g., authenticate user)
            user = Users.query.filter_by(email=login_email).first()
            # print(user.id)
            if user and user.password == login_password:
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash('Login unsuccessful. Please check your username and password.', 'danger')

            # Redirect to a new page or perform other actions

        elif 'registerName' in request.form and 'registerEmail' in request.form and 'registerPassword' in request.form:
            # Registration request
            register_name = request.form.get('registerName')
            register_email = request.form.get('registerEmail')
            register_password = request.form.get('registerPassword')
            confirm_password = request.form.get('confirmPassword')
            # Process registration data here (e.g., create a new user)
            if register_password == confirm_password:
                user = Users(
                    name=register_name,
                    email=register_email,
                    password=register_password
                )
                db.session.add(user)
                db.session.commit()
                flash('You have successfully created an account!')
            else:
                flash('Registration unsuccessful. Passwords Do Not Match!', 'danger')

            # Redirect to a new page or perform other actions

    return render_template("login.html")

@application.route('/home')
@login_required
def home():
    # RMA Live counter
    username = None
    current = current_user._get_current_object()
    if " " in current.name:
        username = current.name.split(" ")[0].capitalize()
    else:
        username = current.name
    rmas = RmaTool.query.order_by(RmaTool.MAT_RMA_ID).all()
    rma_id_list = []
    for rma in rmas:
        rma_id_list.append(rma.MAT_RMA_ID)
    year_freq = {}
    for item in rma_id_list:
        year = item.split('-')[2]  # Extract the year from the ID
        if year in year_freq:
            year_freq[year] += 1  # Increment the count for the year
        else:
            year_freq[year] = 1  # Add the year to the dictionary with a count of 1
    open_rm_ids = db.session.query(RmaTool.MAT_RMA_ID) \
        .filter_by(open_closed="Open") \
        .all()
    closed_rm_ids = db.session.query(RmaTool.MAT_RMA_ID) \
        .filter_by(open_closed="Closed") \
        .all()
    closed_rma_freq = {}
    for item in closed_rm_ids:
        id = item[0]
        YEAR = id.split('-')[2]
        if YEAR in closed_rma_freq:
            closed_rma_freq[YEAR] += 1
        else:
            closed_rma_freq[YEAR] = 1
    open_rma_freq = {}
    for item in open_rm_ids:
        id = item[0]
        YEAR = id.split('-')[2]
        if YEAR in open_rma_freq:
            open_rma_freq[YEAR] += 1
        else:
            open_rma_freq[YEAR] = 1

    # Trials live counter
    trials = Trials.query.order_by(Trials.trial_id).all()
    trial_year_list = [item.trial_year for item in trials if item.trial_year != '']
    print(trial_year_list)
    trial_year_freq = {}
    for item in trial_year_list:
        if item in trial_year_freq:
            trial_year_freq[item] += 1  # Increment the count for the year
        else:
            trial_year_freq[item] = 1  # Add the year to the dictionary with a count of 1
    open_trial_ids = db.session.query(Trials.trial_year) \
        .filter_by(status="Open") \
        .all()
    closed_trial_ids = db.session.query(Trials.trial_year) \
        .filter_by(status="Closed") \
        .all()
    closed_trial_freq = {}
    for item in closed_trial_ids:
        YEAR = item[0]
        if YEAR in closed_trial_freq:
            closed_trial_freq[YEAR] += 1
        else:
            closed_trial_freq[YEAR] = 1
    open_trial_freq = {}
    for item in open_trial_ids:
        YEAR = item[0]
        if YEAR in open_trial_freq:
            open_trial_freq[YEAR] += 1
        else:
            open_trial_freq[YEAR] = 1

    # Project live counter
    projects = Projects.query.order_by(Projects.project_id).all()
    project_year_list = [item.project_year for item in projects if item.project_year != '']
    project_year_freq = {}
    for item in project_year_list:
        if item in project_year_freq:
            project_year_freq[item] += 1  # Increment the count for the year
        else:
            project_year_freq[item] = 1  # Add the year to the dictionary with a count of 1
    open_projects_ids = db.session.query(Projects.project_year) \
        .filter_by(status="Open") \
        .all()
    closed_project_ids = db.session.query(Projects.project_year) \
        .filter_by(status="Closed") \
        .all()
    closed_project_freq = {}
    for item in closed_project_ids:
        YEAR = item[0]
        if YEAR in closed_project_freq:
            closed_project_freq[YEAR] += 1
        else:
            closed_project_freq[YEAR] = 1
    open_project_freq = {}
    for item in open_projects_ids:
        YEAR = item[0]
        if YEAR in open_project_freq:
            open_project_freq[YEAR] += 1
        else:
            open_project_freq[YEAR] = 1

    # TechSupport live counter
    tickets = TechSupport.query.order_by(TechSupport.ticket_id).all()
    ticket_year_list = [item.ticket_year for item in tickets if item.ticket_year != '']
    ticket_year_freq = {}
    for item in ticket_year_list:
        if item in ticket_year_freq:
            ticket_year_freq[item] += 1  # Increment the count for the year
        else:
            ticket_year_freq[item] = 1  # Add the year to the dictionary with a count of 1
    open_ticket_ids = db.session.query(TechSupport.ticket_year) \
        .filter_by(open_closed="Open") \
        .all()
    closed_ticket_ids = db.session.query(TechSupport.ticket_year) \
        .filter_by(open_closed="Closed") \
        .all()
    closed_ticket_freq = {}
    for item in closed_ticket_ids:
        YEAR = item[0]
        if YEAR in closed_ticket_freq:
            closed_ticket_freq[YEAR] += 1
        else:
            closed_ticket_freq[YEAR] = 1
    open_ticket_freq = {}
    for item in open_ticket_ids:
        YEAR = item[0]
        if YEAR in open_ticket_freq:
            open_ticket_freq[YEAR] += 1
        else:
            open_ticket_freq[YEAR] = 1

    return render_template("home.html", year_freq=year_freq, closed_rmas=closed_rma_freq, open_rmas=open_rma_freq,
                           trial_year_freq=trial_year_freq, open_trials=open_trial_freq, closed_trials=closed_trial_freq,
                           project_year_freq=project_year_freq, open_projects=open_project_freq, closed_projects=closed_project_freq,
                           ticket_year_freq=ticket_year_freq, open_tickets=open_ticket_freq, closed_tickets=closed_ticket_freq,
                           username=username)



if __name__ == '__main__':
    application.run()
