const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(bodyParser.json());

// Mock Database
let db = {
    individuals: [
        {
            id: 'I1',
            name: 'الشيخ محمد الحياني',
            familyId: 'F1',
            parentId: null,
            role: 'عميد القبيلة',
            location: [24.7136, 46.6753],
            isVerified: true
        },
        {
            id: 'I2',
            name: 'أحمد بن محمد الحياني',
            familyId: 'F1',
            parentId: 'I1',
            role: 'عضو',
            location: [24.7136, 46.6753],
            isVerified: true
        },
        {
            id: 'I3',
            name: 'سلطان بن محمد الحياني',
            familyId: 'F1',
            parentId: 'I1',
            role: 'عضو',
            location: [24.8136, 46.7753],
            isVerified: true
        }
    ],
    families: [
        { id: 'F1', name: 'عائلة آل فلان', branch: 'الرئيسي', location: 'الرياض' },
        { id: 'F2', name: 'عائلة آل علان', branch: 'الغربي', location: 'جدة' }
    ],
    documents: [
        { id: 'DOC1', title: 'صك النسب الشرعي', type: 'وثيقة رسمية', ownerId: 'I1', hash: '0x3A7F92B1C', timestamp: new Date().toISOString() }
    ],
    events: [
        { id: 'E1', title: 'اجتماع العيد السنوي', date: '2024-04-10', desc: 'اجتماع عام لكافة أفراد القبيلة في ديوان الرياض للعام الهجري الحالي.', location: 'الرياض' }
    ]
};

// Individuals
app.get('/api/individuals', (req, res) => res.json(db.individuals));
app.post('/api/individuals', (req, res) => {
    const newInd = {
        name: req.body.name,
        familyId: req.body.familyId,
        parentId: req.body.parentId || null,
        role: req.body.role || 'عضو',
        location: req.body.location || null,
        isVerified: req.body.isVerified || false,
        id: 'I' + Date.now()
    };
    db.individuals.push(newInd);
    res.status(201).json(newInd);
});
app.delete('/api/individuals/:id', (req, res) => {
    db.individuals = db.individuals.filter(i => i.id !== req.params.id);
    res.status(204).send();
});

// Families
app.get('/api/families', (req, res) => res.json(db.families));
app.post('/api/families', (req, res) => {
    const newFam = {
        name: req.body.name,
        branch: req.body.branch || 'عام',
        location: req.body.location || '',
        id: 'F' + Date.now()
    };
    db.families.push(newFam);
    res.status(201).json(newFam);
});

// Documents
app.get('/api/documents', (req, res) => res.json(db.documents));

// Events
app.get('/api/events', (req, res) => res.json(db.events));

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
