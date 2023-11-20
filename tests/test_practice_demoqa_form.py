import os
from selene import browser, have, be


def test_student_registration_form(browser_config):
    browser.open("/automation-practice-form")

    #WHEN


    browser.element("#firstName").click().should(be.blank).type("Diana")
    browser.element("#lastName").click().should(be.blank).type("Sagaeva")
    browser.element("#userEmail").click().should(be.blank).type("d_sagaeva@mail.ru")
    browser.all(".custom-radio").element_by(have.text("Female")).click()
    browser.element("#userNumber").click().should(be.blank).type("8000000000")
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__year-select").click()
    browser.element('[value="2001"]').click()
    browser.element("[class*=month-select]").click()
    browser.element('[class*=month-select] [value="5"]').click()
    browser.element("[class*=day--012]").click()
    browser.element("#subjectsInput").click().type("Accoun").press_tab()
    browser.element("[for=hobbies-checkbox-3]").click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("../picture/tony.jpg"))
    browser.element("#currentAddress").click().should(be.blank).type("Karlskoga 66")
    browser.element("#react-select-3-input").type("Haryana").press_enter()
    browser.element("#react-select-4-input").type("Panipat").press_enter()
    browser.element("#submit").press_enter()

    #THEN


    browser.all("tbody tr td")[1::2].should(
        have.texts(
            "Diana Sagaeva",
            "d_sagaeva@mail.ru",
            "Female",
            "8000000000",
            "12 June,2001",
            "Accounting",
            "Music",
            "tony.jpg",
            "Karlskoga 66",
            "Haryana Panipat",
        )
    )
